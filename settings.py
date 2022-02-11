from os import environ

SESSION_CONFIG_DEFAULTS = {"real_world_currency_per_point": 0.007, "participation_fee": 5}
SESSION_CONFIGS = [
    {
        "name": "KnapSack",
        "display_name": "KnapSack",
        "num_demo_participants": 1,
        "app_sequence": ["KnapSack"],
    },

{
        "name": "Maze",
        "display_name": "Maze",
        "num_demo_participants": 1,
        "app_sequence": ["Maze"],
    },

    {
        "name": "Travelling_Salesperson",
        "display_name": "Travelling_Salesperson",
        "num_demo_participants": 1,
        "app_sequence": ["Travelling_Salesperson"],
    },


]

LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "AUD"
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ""



ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'Curtin20'

SECRET_KEY = "blahblah"

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ["otree"]

EXTENSION_APPS = ['otree_tools']

