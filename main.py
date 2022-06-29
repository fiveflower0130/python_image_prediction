import os
import uvicorn
import pytest
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from image_prediction_mutithreading import TestPredictionThread

app = FastAPI()

image_prediction = TestPredictionThread()
execution_path = os.getcwd()
model_path = os.path.join(execution_path, "idenprof", "models")
json_path = os.path.join(execution_path, "idenprof", "json")
prediction_path = os.path.join(execution_path, "prediction_result")
test_info = {
    "model_path": model_path,
    "json_path": json_path,
    "prediction_path": prediction_path
}

image_prediction.set_test_info(test_info)
image_prediction.set_prediction()


class PredictionInfo(BaseModel):
    path: str
    # thread_num: Optional[str] = "1"
    # model_type: Optional[str] = "ResNet"
    # muti_thread: Optional[bool] = False


# API文件中定義的回傳格式
def resp(errMsg, data=None):
    resp = {'code': "0", 'message': ""}

    if errMsg is not None:
        resp['code'] = "1"
        resp['message'] = errMsg
    else:
        resp['data'] = data

    return resp


@app.get("/")
def read_root():
    return {"data": "Hello World"}


@app.post("/image/prediction")
def get_image_prediction(body: PredictionInfo):
    '''取得AI image prediction的結果\n

        Args:\n
            test_path: 欲測試圖片之路徑或是資料夾\n
        Response:\n
            code: 執行API結果; 0 = 成功, 1 = 失敗\n
            message: 執行結果; 成功=空字串, 失敗=錯誤訊息\n
            data: 回傳所有Prediction的結果，包含圖片資料、預測結果、預測數據\n
    '''
    test_path = body.path
    if not test_path or not isinstance(test_path, str):
        return resp("please check your path")
    try:
        data = image_prediction.images_prediction(test_path)
    except Exception as err:
        return resp(str(err))
    finally:
        return resp(None, data)


if __name__ == "__main__":
    pytest.main(['--html=report/report.html', 'test_main.py'])
    uvicorn.run(app, host="0.0.0.0", port=8007)
