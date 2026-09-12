#!/usr/bin/env python3
import argparse, csv, json
from collections import defaultdict

def number(value):
    try:
        return float(str(value).replace(',', '').strip()) if str(value).strip() else 0.0
    except (TypeError, ValueError):
        return 0.0

def ratio(a, b):
    return round(a / b * 100, 2) if b else None

def read_csv(path):
    if not path:
        return []
    with open(path, encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))

def social_summary(rows):
    totals = defaultdict(lambda: defaultdict(float))
    fields = ['views','reach','likes','comments','shares','saves','followers_gained',
              'watch_time_seconds','profile_visits','link_clicks','inquiries']
    for row in rows:
        platform = (row.get('platform') or 'unknown').lower().strip()
        totals[platform]['posts'] += 1
        for field in fields:
            totals[platform][field] += number(row.get(field))
    result = {}
    for platform, t in totals.items():
        engagements = t['likes'] + t['comments'] + t['shares'] + t['saves']
        result[platform] = dict(t)
        result[platform].update({
            'engagement_rate_pct': ratio(engagements, t['reach']),
            'share_rate_pct': ratio(t['shares'], t['reach']),
            'save_rate_pct': ratio(t['saves'], t['reach']),
            'action_rate_pct': ratio(t['link_clicks'] + t['inquiries'], t['reach'])
        })
    return result

def web_summary(rows):
    fields = ['users','sessions','organic_sessions','engaged_sessions','whatsapp_clicks',
              'event_form_starts','event_form_submits','booking_starts','bookings']
    totals = {field: 0.0 for field in fields}
    for row in rows:
        for field in fields:
            totals[field] += number(row.get(field))
    totals.update({
        'engagement_rate_pct': ratio(totals['engaged_sessions'], totals['sessions']),
        'whatsapp_rate_pct': ratio(totals['whatsapp_clicks'], totals['sessions']),
        'event_form_conversion_pct': ratio(totals['event_form_submits'], totals['event_form_starts']),
        'booking_conversion_pct': ratio(totals['bookings'], totals['booking_starts'])
    })
    return totals

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--social')
    parser.add_argument('--web')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    payload = {
        'social': social_summary(read_csv(args.social)),
        'web': web_summary(read_csv(args.web)),
        'warnings': ['Las tasas null no tienen denominador disponible.']
    }
    with open(args.output, 'w', encoding='utf-8') as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
