# python_image_prediction

Using imageAI to prediction image and make web API by FASTAPI.

_© 2022 Dante
## Installation and Execution

### 1. Install pip package

run `pip install -r requirement.txt`

if pip not work please run `python -m pip install --upgrade pip`

### 2. Run FastAPI service
run `python main.py` start FASTAPI service,

or you can try another way with command line

run `uvicorn main:app --reload --host 0.0.0.0 --port 8007`

### 3. Check API Document
If server run correctly, check the API document on `http://127.0.0.1:8000/docs`
or you can check it by txt file by `http://127.0.0.1:8000/redoc`

### 4. Package to private network
If you want to run it on private network or close environment, run `pyinstaller -F main.py`.
then take `main.exe` from `dict` folder and copy `idenprof` at same folder.