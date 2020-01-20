# Description

Testing of https://vk.com/dev/likes methods

## Install

1) Use ```install.sh``` for installation, or follow the same logic to create initial setup. (_Take time to look up the install.sh script before usage_)

```bash
# Linux or MacOS
chmod u+x install.sh
./install.sh
```

2) Follow the https://vk.com/dev/access_token to obtain the access_token.

3) Fill the .env file in root of the project with the following:

```bash
ACCESS_TOKEN={YOUR_ACCESS_TOKEN}
USER_ID={APP_USER_ID} # Standalone-app id
VK_USER_ID={VK_USER_ID} # Your vk user id
```

## Run

```bash
pytest tests/
```

## Report generation

Allure report is generated after each run into allure-report folder. To generate the report follow https://docs.qameta.io/allure/#_pytest
