from django.core.management.base import BaseCommand
from results.models import Area, Category, Event, Result

class Command(BaseCommand):
    help = 'Populate initial data for Family Fiesta 2025'

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
                "Smiling Competition",
                "Picking up sweets",
                "Colouring Competition"
            ],
            "Above 5 & below 12 years": [
                "Drawing Competition (Pencil Sketch)",
                "Walk by Faith",
                "Song Solo: 279 enikkayorthama sampath"
            ],
            "Above 12 & below 18 years": [
                "Drawing Competition (Pencil Sketch)",
                "Walk by Faith",
                "Song Solo: 201 Yesuvin thiruppaadathil",
                "Speech - 3 minutes"
            ],
            "Above 18 & below 30 years": [
                "Song Solo: 73 Paadum Parama Rakhsakan Yesuve",
                "Speech - 4 minutes",
                "Essay Writing - 30 minutes",
                "Instant Bible Reading"
            ],
            "Above 30 & below 60 years": [
                "Song Solo: 184 Thanaya Ninnude Perkkaayi",
                "Speech - 4 minutes",
                "Essay Writing - 30 minutes",
                "Instant Bible Reading"
            ],
            "Above 60 years": [
                "Song Solo: 299 Modam athi modam modam",
                "Walk by Faith",
                "Speech - 4 minutes",
                "Scripture: Spot & Read"
            ],
            "Group Items": [
                "Group Song - 436 Nin Daanam njaan Anubhavichu / 380 En Kristhan Yodhaavaakuvaan",
                "Cooking Without Fire",
                "Skit"
            ]
        }

        for cat_name, events_list in categories_with_events.items():
            category, _ = Category.objects.get_or_create(name=cat_name)
            for event_name in events_list:
                event, _ = Event.objects.get_or_create(name=event_name, category=category)
                for pos in [1, 2, 3]:
                    Result.objects.get_or_create(
                        event=event,
                        position=pos,
                        defaults={
                            'name': 'Results to be announced',
                            'area': None
                        }
                    )

        self.stdout.write(self.style.SUCCESS('✅ Areas, Categories, Events, and default Results populated successfully!'))
