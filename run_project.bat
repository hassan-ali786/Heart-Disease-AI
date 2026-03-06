@echo off
echo Training Heart Disease Model...
python train_model.py

echo Starting Web Application...
python app.py

pause