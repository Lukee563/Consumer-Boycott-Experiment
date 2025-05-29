from os import environ

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

SESSION_CONFIGS = [
    dict(
        name='consumer_study_final',
        display_name="Consumer Boycott Experiment",
        num_demo_participants=4,
        app_sequence=['consumer_study'],
    ),
]

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin')

DEMO_PAGE_INTRO_HTML = ""
SECRET_KEY = 'your-secret-key'

INSTALLED_APPS = ['otree']