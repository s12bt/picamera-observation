This fixed-point observation system take pictures by Raspberry Pi + camera module and upload to Google Drive.

## Requirement
- Raspberry Pi3 model B+
- Raspberry Pi3 camera module
- Google account
- python3

## Installation
- Get Google OAuth client id and secret key.
- Fill `client_id` and `client_secret` in `settings.yaml`.
- Fill your environment info, `save_directory_path` and `google_drive_folder_id` in `camera.py`.
- `pip3 install google-api-python-client PyDrive`
- Run `camera.py`
  - First run, show authorization page URL on console. Access the URL and get authorization code.
