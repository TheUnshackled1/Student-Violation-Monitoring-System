from django.core.management.base import BaseCommand
from violations.models import ViolationType


class Command(BaseCommand):
    help = "Seed initial violation types (Major and Minor offenses)"

    def handle(self, *args, **options):
        # Clear existing violation types if requested
        if options.get("clear"):
            ViolationType.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared all existing violation types."))

        major_offenses = [
            {
                "name": "Improper wearing/mutilation or tampering of ID",
                "code": "MO-01",
                "description": "Includes improper display, alteration, or damage to student identification card",
            },
            {
                "name": "Fighting, violence-oriented fraternities/sororities related activities within school premises or activities involving students",
                "code": "MO-02",
                "description": "Physical altercations or gang-related activities on campus",
            },
            {
                "name": "Dishonesty in any form",
                "code": "MO-03",
                "description": "Includes cheating, fraud, forgery, and other forms of academic or personal dishonesty",
            },
            {
                "name": "Vandalism",
                "code": "MO-04",
                "description": "Intentional destruction or damage to school property or facilities",
            },
            {
                "name": "Theft",
                "code": "MO-05",
                "description": "Taking property belonging to others without permission",
            },
            {
                "name": "Drugs (using/pushing/possessing)",
                "code": "MO-06",
                "description": "Illegal drug use, distribution, or possession within school premises",
            },
            {
                "name": "Deadly weapons (carrying/possessing)",
                "code": "MO-07",
                "description": "Possession or carrying of weapons capable of causing harm",
            },
            {
                "name": "Immorality",
                "code": "MO-08",
                "description": "Acts against moral standards and decency within school premises",
            },
            {
                "name": "Extortion/Bullying/Intimidation",
                "code": "MO-09",
                "description": "Threatening, coercing, or harassing other students or staff",
            },
            {
                "name": "Public scandal/any act that would put school in bad light",
                "code": "MO-10",
                "description": "Actions that damage the reputation of the institution",
            },
            {
                "name": "Subversive activities against school management/school policies",
                "code": "MO-11",
                "description": "Organizing or participating in activities that undermine school authority",
            },
            {
                "name": "Smoking/vaping within school premises",
                "code": "MO-12",
                "description": "Use of cigarettes, e-cigarettes, or vaping devices on campus",
            },
            {
                "name": "Gross act of disrespect toward school personnel",
                "code": "MO-13",
                "description": "Severe disrespectful behavior toward faculty, staff, or administrators",
            },
            {
                "name": "Alcohol drinking inside school premises",
                "code": "MO-14",
                "description": "Consumption of alcoholic beverages within school grounds",
            },
        ]

        minor_offenses = [
            {
                "name": "Gambling within the school/vicinity",
                "code": "MiO-01",
                "description": "Engaging in gambling activities on or near school premises",
            },
            {
                "name": "Non-wearing of ID or lending of ID to another person",
                "code": "MiO-02",
                "description": "Failure to wear student ID or allowing others to use your ID",
            },
            {
                "name": "Littering",
                "code": "MiO-03",
                "description": "Improper disposal of trash or waste on school premises",
            },
            {
                "name": "Any form of unauthorized posting within school premises or PPA's",
                "code": "MiO-04",
                "description": "Posting materials without proper approval from authorities",
            },
            {
                "name": "Any unauthorized collection of money",
                "code": "MiO-05",
                "description": "Collecting fees or donations without proper authorization",
            },
            {
                "name": "Loitering",
                "code": "MiO-06",
                "description": "Lingering in unauthorized areas or during class hours without valid reason",
            },
            {
                "name": "Violation of library rules",
                "code": "MiO-07",
                "description": "Not following established library policies and procedures",
            },
        ]

        created_count = 0
        updated_count = 0

        # Create Major Offenses
        for offense in major_offenses:
            obj, created = ViolationType.objects.update_or_create(
                code=offense["code"],
                defaults={
                    "name": offense["name"],
                    "category": "major",
                    "description": offense.get("description", ""),
                    "is_active": True,
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        # Create Minor Offenses
        for offense in minor_offenses:
            obj, created = ViolationType.objects.update_or_create(
                code=offense["code"],
                defaults={
                    "name": offense["name"],
                    "category": "minor",
                    "description": offense.get("description", ""),
                    "is_active": True,
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded violation types: {created_count} created, {updated_count} updated."
            )
        )

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing violation types before seeding",
        )
