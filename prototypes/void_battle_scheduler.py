# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from datetime import datetime
import test_input


# %%
achievements = test_input.event["achievements"]
achievements

# %%
end_date = datetime.strptime(
    test_input.event["end_date"], "%Y-%m-%d")
end_date

#%%
time_remaining = end_date - datetime.now()
hours_remaining, remainder = divmod(time_remaining.seconds, 3600)
hours_remaining += time_remaining.days * 24
minutes, seconds = divmod(remainder, 60)
print(hours_remaining, minutes, seconds)


# %%
current_stam = 120
current_wings = 5
max_stam = 120

# Real regen: 10/h; Honey Tea: 2/h
total_remaining_stam = current_stam + 12 * hours_remaining + minutes // 6 + minutes // 30
total_remaining_stam


# %%
cost_to_finish = sum([i['remaining'] * i['stam_cost'] for i in achievements])
cost_to_finish


# %%
total_difference = cost_to_finish - total_remaining_stam
total_difference


# %%
[i["title"] for i in achievements]


# %%
f = [i["title"] for i in achievements]
double_drops = test_input.event["double_drops"]

double_drops = [[f[j] for j in i] for i in double_drops]

from datetime import date, timedelta, time
from dateutil.rrule import rrule, DAILY

a = datetime.now()
b = end_date

double_drops_dict = {}

for index, dt in enumerate(rrule(DAILY, dtstart=a, until=b)):
    double_drops_dict[dt.strftime("%Y-%m-%d")] = {
        "double_drops": double_drops[index],
        "remaining_stam": 12*24 - 15*3 - 20*2 - 25*2,
        "remaining_wings": 24
    }

hours_left_today = datetime.combine(date.today() + timedelta(days=1), time.min) - datetime.now()
hours_left_today = hours_left_today.seconds // 3600
double_drops_dict[datetime.now().strftime("%Y-%m-%d")]["remaining_stam"] = current_stam + 10*hours_left_today
double_drops_dict[datetime.now().strftime("%Y-%m-%d")]["remaining_wings"] = current_wings + hours_left_today 
double_drops_dict


# %%
import copy

track_achieves = copy.deepcopy(achievements)
remaining_stamina = 0
remaining_wings = 0
prospective_schedule = {}
prospective_schedule["schedule"] = []
for i in double_drops_dict.keys():
    todays_schedule = {}
    todays_schedule["date"] = i
    # display(HTML(f"<h2>Prospective Schedule for {i}</h2><details><summary>Click to expand</summary>Some text</details>"))
    todays_stam = double_drops_dict[i]["remaining_stam"]
    todays_wings = double_drops_dict[i]["remaining_wings"]
    todays_schedule["stamina_wings"] = [
        {"Type": "Stamina", "Regened": todays_stam, "Remaining": remaining_stamina},
        {"Type": "Wings", "Regened": todays_wings, "Remaining": remaining_wings}]
    todays_stam += remaining_stamina
    todays_wings += remaining_wings
    todays_double_drops = double_drops_dict[i]["double_drops"]
    prospective_fights = [i for i in track_achieves if i["remaining"] > 0 and i["title"] in todays_double_drops]
    todays_schedule["potential_2x_fights"] = prospective_fights
    stam_costs = [i["stam_cost"] for i in prospective_fights]
    stam_costs.sort(reverse=True)
    fights_to_run = []
    while stam_costs and any([True for i in track_achieves if i["title"] in todays_double_drops and i["remaining"] > 0]) and todays_stam > min(stam_costs):
        for stam in stam_costs:
            wing_cost = 3 if stam == 30 else 2
            if stam > todays_stam:
                if wing_cost > todays_wings:
                    continue
            for fight in track_achieves:
                if fight["stam_cost"] != stam or fight["remaining"] <= 0 or not fight["title"] in todays_double_drops:
                    continue
                runs = min(todays_stam // stam, fight["remaining"])
                fight["remaining"] -= runs
                coops = min(todays_wings // wing_cost, fight["remaining"])
                fights_to_run.append(
                    {"Title": fight["title"], "Solo Runs": runs, "Coops": coops, "Stamina": stam*runs, "Wings": coops*wing_cost})
                fight["remaining"] -= coops
                break
            todays_stam -= runs*stam
            todays_wings -= coops*wing_cost
    remaining_stamina = todays_stam if stam_costs else 0
    remaining_wings = min(todays_wings, 2)
    if todays_wings - remaining_wings > 0:
        fights_to_run.append(
            {"Title": "Dragon Trials", "Solo Runs": "", "Coops": "", "Stamina": "", "Wings": todays_wings - remaining_wings})
    if not stam_costs:
        fights_to_run.append({"Title": "Solo Stuff", "Solo Runs": "", "Coops": "", "Stamina": todays_stam, "Wings": ""})
    todays_schedule["fights_to_run"] = fights_to_run
    todays_schedule["remaining_stamina_wings"] = [
        {"Remaining": "Stamina", "Qty": remaining_stamina}, 
        {"Remaining": "Wings", "Qty": remaining_wings}]
    prospective_schedule["schedule"].append(todays_schedule)

prospective_schedule["remaining_fights"] = [i for i in track_achieves if i['remaining'] > 0]
prospective_schedule["missing_stam"] = sum([i["stam_cost"] * i["remaining"] for i in track_achieves])
# print("Required Stamina:", missing_stam, "=", missing_stam / 30, "big honeys.")
print(prospective_schedule)


# %%


