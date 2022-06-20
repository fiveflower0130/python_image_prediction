# python_image_prediction

Using imageAI to prediction image and make web API by FASTAPI.

_© 2022 Dante
## Installation and Execution

### environment
python version: v3.7\n
extension of folder idenprof: link `https://drive.google.com/drive/folders/1CW0j2uOgdNZU7iCe9odZbnkdosdMNMRV?usp=sharing`

### 1. Install pip package
please run `python -m pip install --upgrade pip` first,\n
then run `pip install -r requirement.txt`

### 2. Run FastAPI service
run `python main.py` start FASTAPI service,\n
or you can try another way with command line\n
run `uvicorn main:app --reload --host 0.0.0.0 --port 8007`

### 3. Check API Document
If server run correctly, check the API document on `http://127.0.0.1:8000/docs`\n
or you can check it by txt file by `http://127.0.0.1:8000/redoc`

### 4. Package to private network
If you want to run it on private network or close environment, run `pyinstaller -F main.py`\n
then take `main.exe` from `dict` folder and copy `idenprof` at same folder.