# Description

Testing of https://vk.com/dev/likes methods

## Install

Take time to look up the install.sh script before usage.

```bash
# Linux or MacOS
chmod u+x install.sh
./install.sh
```

1) Before usage follow the https://vk.com/dev/access_token to get the access_token.

2) Fill the file .env in root of the project with the following lines

```bash
ACCESS_TOKEN={YOUR_TOKEN}
USER_ID={APP_USER_ID} # Standalone-app id
VK_USER_ID={VK_USER_ID} # Your vk user id
```

## Run

```bash
pytest tests/
```

## Report generation

Allure report generates allure-report folder after each run.

To generate report follow https://docs.qameta.io/allure/#_pytest
