# Template module for AllianceAuth.<a name="aa-industries"></a>

A Industries tool for Alliance Auth
_______________________________________________________________________

- [AA Template](#aa-industries)
  - [Features](#features)
  - [Upcoming](#upcoming)
  - [Installation](#features)
    - [Step 1 - Install the Package](#step1)
    - [Step 2 - Configure Alliance Auth](#step2)
    - [Step 3 - Add the Scheduled Tasks and Settings](#step3)
    - [Step 4 - Migration to AA](#step4)
    - [Step 5 - Setting up Permissions](#step5)
    - [Step 6 - (Optional) Setting up Compatibilies](#step6)
  - [Highlights](#highlights)

## Features<a name="features"></a>

## Upcoming<a name="upcoming"></a>
- Production Interface
- RAW Material Information for each Blueprint
- Notification for Production are finished

## Installation<a name="installation"></a>

> [!NOTE]
> AA Template needs at least Alliance Auth v4.6.0
> Please make sure to update your Alliance Auth before you install this APP

### Step 1 - Install the Package<a name="step1"></a>

Make sure you're in your virtual environment (venv) of your Alliance Auth then install the pakage.

```shell
pip install aa-industries
```

### Step 2 - Configure Alliance Auth<a name="step2"></a>

Configure your Alliance Auth settings (`local.py`) as follows:

- Add `'allianceauth.corputils',` to `INSTALLED_APPS`
- Add `'eveuniverse',` to `INSTALLED_APPS`
- Add `'industries',` to `INSTALLED_APPS`

### Step 3 - Add the Scheduled Tasks<a name="step3"></a>

To set up the Scheduled Tasks add following code to your `local.py`

```python
CELERYBEAT_SCHEDULE["industries_update_all_industries"] = {
    "task": "industries.tasks.update_all_industries",
    "schedule": crontab(minute=0, hour="*/1"),
}
```

### Step 4 - Migration to AA<a name="step4"></a>

```shell
python manage.py collectstatic
python manage.py migrate
```

### Step 5 - Setting up Permissions<a name="step5"></a>

With the Following IDs you can set up the permissions for the Template

| ID             | Description                    |                                                          |
| :------------- | :----------------------------- | :------------------------------------------------------- |
| `basic_access` | Can access the Template module | All Members with the Permission can access the Template. |

### Step 6 - (Optional) Setting up Compatibilies<a name="step6"></a>

The Following Settings can be setting up in the `local.py`

- INDUSTRIES_APP_NAME: `"YOURNAME"` - Set the name of the APP

- INDUSTRIES_LOGGER_USE: `True / False` - Set to use own Logger File

If you set up INDUSTRIES_LOGGER_USE to `True` you need to add the following code below:

```python
LOGGING_INDUSTRIES = {
    "handlers": {
        "industries_file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "log/industries.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
        },
    },
    "loggers": {
        "industries": {
            "handlers": ["industries_file", "console"],
            "level": "INFO",
        },
    },
}
LOGGING["handlers"].update(LOGGING_INDUSTRIES["handlers"])
LOGGING["loggers"].update(LOGGING_INDUSTRIES["loggers"])
```

## Highlights<a name="highlights"></a>

> [!NOTE]
> Contributing
> You want to improve the project?
> Just Make a [Pull Request](https://github.com/Geuthur/aa-industries/pulls) with the Guidelines.
> We Using pre-commit
