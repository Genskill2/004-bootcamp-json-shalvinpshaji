import json
import collections

def load_journal(file_name):
    with open(file_name,'r') as f:
        activity = json.load(f)
    return activity

load_journal('journal.json')
def compute_phi(file_name, event):

    activities = load_journal(file_name=file_name)
    d = collections.defaultdict(int)
    for e in activities:
        if e['squirrel']:
            d['np1'] += 1
            if event in e['events']:
                d['n11'] += 1
                d['n1p'] += 1
            else:
                d['n01'] += 1
                d['n0p'] += 1
        else:
            d['np0'] += 1
            if event in e['events']:
                d['n10'] += 1
                d['n1p'] += 1
            else:
                d['n00'] += 1
                d['n0p'] += 1
    phi = (d['n11'] * d['n00'] - d['n10'] * d['n01'])/ ((d['n1p'] * d['n0p'] * d['np1'] * d['np0'])**0.5)
    return phi

def compute_correlations(file_name):
    activities = load_journal(file_name=file_name)
    correlations = {}
    for day in activities:
        for event in day['events']:
            if event not in correlations.keys():
                correlations[event] = compute_phi(file_name,event)
    return correlations

def diagnose(file_name):
    correlations = compute_correlations(file_name)
    positive_max = max(correlations, key=correlations.get)
    negetive_max = min(correlations, key=correlations.get)
    return positive_max, negetive_max


if __name__ == '__main__':
    diagnose('journal.json')