# pip vs uv — Notes

## pip workflow
1. python -m venv venv
2. venv\Scripts\activate
3. pip install requests
4. deactivate

## uv workflow
1. uv venv
2. venv\Scripts\activate
3. uv pip install requests
4. uv pip freeze > requirements.txt
5. deactivate


===========================================Difference table=========================================

|            Task            |               pip               |                 uv                 |
| ---------------------------|-------------------------------- | ---------------------------------- |
| Create Virtual Environment | `python -m venv venv`           | `uv venv`                          |
| Install Package            | `pip install requests`          | `uv pip install requests`          |
| Generate requirements.txt  | `pip freeze > requirements.txt` | `uv pip freeze > requirements.txt` |
| Speed                      | Normal                          | Much Faster (up to 10x+)           |
| ---------------------------|-------------------------------- | ---------------------------------- |