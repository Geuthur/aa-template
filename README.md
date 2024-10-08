# Template module for AllianceAuth.<a name="aa-template"></a>

> \[!DANGER\]
> Before you create Models, etc remove the 0001_initial.py from migrations folder if you dont have created own one.

A Template App that templating template to template

______________________________________________________________________

- [AA Template](#aa-template)
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

## Installation<a name="installation"></a>

> \[!NOTE\]
> AA Template needs at least Alliance Auth v4.0.0
> Please make sure to update your Alliance Auth before you install this APP

### Step 1 - Install the Package<a name="step1"></a>

Make sure you're in your virtual environment (venv) of your Alliance Auth then install the pakage.

```shell
pip install aa-template
```

### Step 2 - Configure Alliance Auth<a name="step2"></a>

Configure your Alliance Auth settings (`local.py`) as follows:

- Add `'allianceauth.corputils',` to `INSTALLED_APPS`
- Add `'eveuniverse',` to `INSTALLED_APPS`
- Add `'template',` to `INSTALLED_APPS`

### Step 3 - Add the Scheduled Tasks<a name="step3"></a>

To set up the Scheduled Tasks add following code to your `local.py`

```python
CELERYBEAT_SCHEDULE["template_update_all_template"] = {
    "task": "template.tasks.update_all_template",
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

- TEMPLATE_APP_NAME:          `"YOURNAME"`     - Set the name of the APP

- TEMPLATE_LOGGER_USE:        `True / False`   - Set to use own Logger File

If you set up TEMPLATE_LOGGER_USE to `True` you need to add the following code below:

```python
LOGGING_TEMPLATE = {
    "handlers": {
        "template_file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "log/template.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
        },
    },
    "loggers": {
        "template": {
            "handlers": ["template_file", "console"],
            "level": "INFO",
        },
    },
}
LOGGING["handlers"].update(LOGGING_TEMPLATE["handlers"])
LOGGING["loggers"].update(LOGGING_TEMPLATE["loggers"])
```

## Highlights<a name="highlights"></a>

> \[!NOTE\]
> Contributing
> You want to improve the project?
> Just Make a [Pull Request](https://github.com/Geuthur/aa-template/pulls) with the Guidelines.
> We Using pre-commit
