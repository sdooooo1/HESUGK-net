import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("/HESUGK-net/ultralytics-main/ultralytics/cfg/models/11/yolov11_all.yaml")
    model.train(data="/HESUGK-net/ultralytics-main/ultralytics/cfg/datasets/insulator_data.yaml",
                cache=False,
                imgsz=640,
                epochs=150,
                single_cls=False,  # 是否是单类别检测
                batch=16,
                close_mosaic=10,
                workers=0,
                device='2',
                optimizer='SGD',
                amp=True,
                project='runs/train',
                name='exp',
                )
