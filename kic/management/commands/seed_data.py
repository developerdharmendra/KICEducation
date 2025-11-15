from django.core.management.base import BaseCommand, CommandParser

from kic.factories import (
    AchievementFactory,
    WhyStudyFactory,
    StudyReasonFactory,
    CountryFactFactory,
    RequirementFactory,
    CostAndBudgetFactory,
    StepProcessFactory,
    FAQFactory,
    CounsellorFactory,
    MissionFactory,
    ServiceFactory,
    TestimonialFactory,
    TestPreparationClassFactory,
    UniversityFactory,
)


class Command(BaseCommand):
    help = 'Seed database with fake data using django factory boy.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--achievements', type=int, default=10, help='Number of achievements')
        parser.add_argument(
            '--why_study', type=int, default=10, help='Number of why study points for a counry'
        )
        parser.add_argument(
            '--reasons', type=int, default=10, help='Number of reasons to study in a counry'
        )
        parser.add_argument('--facts', type=int, default=10, help='Number of facts about a counry')
        parser.add_argument(
            '--requirements', type=int, default=10, help='Number of requirements about a counry'
        )
        parser.add_argument(
            '--budgets', type=int, default=10, help='Number of cost & budget for a counry'
        )
        parser.add_argument(
            '--step_processes',
            type=int,
            default=10,
            help='Number of step by step process for a counry',
        )
        parser.add_argument('--faqs', type=int, default=10, help='Number of FAQs for a counry')
        parser.add_argument('--counsellors', type=int, default=5, help='Number of counsellors')
        parser.add_argument('--missions', type=int, default=5, help='Number of missions')
        parser.add_argument('--services', type=int, default=5, help='Number of services')
        parser.add_argument('--testimonials', type=int, default=5, help='Number of testimonials')
        parser.add_argument(
            '--preparation_classes', type=int, default=4, help='Number of preparation classes'
        )
        parser.add_argument('--universities', type=int, default=20, help='Number of universities')

    def handle(self, *args, **kwargs):
        achievements = kwargs['achievements']
        why_study = kwargs['why_study']
        reasons = kwargs['reasons']
        facts = kwargs['facts']
        requirements = kwargs['requirements']
        budgets = kwargs['budgets']
        step_processes = kwargs['step_processes']
        faqs = kwargs['faqs']
        missions = kwargs['counsellors']
        missions = kwargs['missions']
        services = kwargs['services']
        testimonials = kwargs['testimonials']
        preparation_classes = kwargs['preparation_classes']
        universities = kwargs['universities']

        # country related data
        WhyStudyFactory.create_batch(why_study)
        StudyReasonFactory.create_batch(reasons)
        CountryFactFactory.create_batch(facts)
        RequirementFactory.create_batch(requirements)
        CostAndBudgetFactory.create_batch(budgets)
        StepProcessFactory.create_batch(step_processes)
        FAQFactory.create_batch(faqs)
        UniversityFactory.create_batch(universities)

        AchievementFactory.create_batch(achievements)
        CounsellorFactory.create_batch(missions)
        MissionFactory.create_batch(missions)
        ServiceFactory.create_batch(services)
        TestimonialFactory.create_batch(testimonials)
        TestPreparationClassFactory.create_batch(preparation_classes)

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))
