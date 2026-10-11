from datetime import date

from django.core.management.base import BaseCommand
from results.models import Area, Category, Event, Result

DAY_1 = date(2026, 10, 11)
DAY_2 = date(2026, 10, 24)


class Command(BaseCommand):
    help = 'Populate initial data for Family Fiesta'

    def handle(self, *args, **kwargs):
        areas = [
            "CHANGAMPUZHA NAGAR",
            "CHURCH AREA",
            "EDAPALLY",
            "NORTH KALAMASSERY",
            "SOUTH KALAMASSERY",
            "UNIVERSITY"
        ]

        for area_name in areas:
            Area.objects.get_or_create(name=area_name)

        categories_with_events = {
            "Below 5 years": [
                ("Picking up sweets", DAY_1),
                ("Bible Character Presentation", DAY_1),
            ],
            "Above 5 & below 12 years": [
                ("Pencil Drawing Competition", DAY_1),
                ("Bible Character Presentation", DAY_1),
                ("Song Solo (Male)", DAY_2),
                ("Song Solo (Female)", DAY_2),
                ("Instrumental Music (Key Board)", DAY_2),
                ("Instrumental Music (Violin)", DAY_2),
                ("Instrumental Music (Guitar)", DAY_2),
            ],
            "Above 12 & below 18 years": [
                ("Song Solo (Male)", DAY_2),
                ("Song Solo (Female)", DAY_2),
                ("Instrumental Music (Key Board)", DAY_2),
                ("Instrumental Music (Violin)", DAY_2),
                ("Instrumental Music (Guitar)", DAY_2),
                ("Just A Minute (JAM)", DAY_1),
                ("Essay Writing", DAY_1),
            ],
            "Above 18 & below 30 years": [
                ("Song Solo (Male)", DAY_2),
                ("Song Solo (Female)", DAY_2),
                ("Just A Minute (JAM)", DAY_1),
                ("Essay Writing", DAY_1),
                ("Instant Bible Reading", DAY_1),
            ],
            "Above 30 & below 60 years": [
                ("Song Solo (Male)", DAY_2),
                ("Song Solo (Female)", DAY_2),
                ("Essay Writing", DAY_1),
                ("Instant Bible Reading", DAY_1),
                ("Just A Minute (JAM)", DAY_1),
            ],
            "Above 60 years": [
                ("Song Solo (Male)", DAY_2),
                ("Song Solo (Female)", DAY_2),
                ("Instant Bible Reading", DAY_1),
                ("Speech (Elocution)", DAY_1),
                ("Essay Writing", DAY_1),
            ],
            "Instrumental Music (Above 18)": [
                ("Key Board", DAY_2),
                ("Violin", DAY_2),
                ("Guitar", DAY_2),
            ],
            "Group Items": [
                ("Group Song", DAY_2),
                ("Family Song", DAY_2),
                ("Cooking Without Fire", DAY_2),
                ("Skit", DAY_2),
            ],
        }

        # Create categories, events (with dates), and blank results
        for cat_name, events_list in categories_with_events.items():
            category, _ = Category.objects.get_or_create(name=cat_name)
            for event_name, event_date in events_list:
                event, _ = Event.objects.update_or_create(
                    name=event_name,
                    category=category,
                    defaults={'date': event_date},
                )
                for pos in [1, 2, 3]:
                    Result.objects.get_or_create(
                        event=event,
                        position=pos,
                        defaults={'name': '', 'area': None}
                    )

        self.stdout.write(self.style.SUCCESS('✅ Areas, Categories, Events (with dates), and blank Results populated successfully!'))