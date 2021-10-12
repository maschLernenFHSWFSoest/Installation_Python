@echo off
REM installation bzw. update der Python Bibliotheken und Jupyter Notebook, 
REM auf den Stand fuer das XOR und die Blumenerkennung ML-Version 1.0
REM MK, 17.11.2019 SH, angepasst fuer tsne 18.11.2019 , AS 21.11.2019 pip version
REM NL, 09.04.2021, angepasst auf neue Versionen
REM SB, 01.07.2021, angepasst fuer Seminarthema Wuerfelerkennung, opencv-python & tqdm
REM JR, 05.08.2021, angepasst an neuere Versionen, Kompatibilität beibehalten
REM please save this file with Encoding in UTF8-ohne-BOM

pip list
echo "this is what you have at the moment on your PC"
echo "Install or update Python libraries" 
echo "Pleace press Ctrl+c to cancel  (ctr.+c um abzubrechen)"
echo "any other key to allow and continue"
pause

REM ML-Version 1.0 fuer Machine Learning Labor Version 2 ohne jupyter notebook

pip install pip==21.1.1
pip install Keras==2.4.3
pip install tensorflow==2.5.0
pip install -U pydicom==1.3.0
pip install pandas==1.2.3
pip install scikit-image==0.16.2

pip install scipy==1.6.1
pip install matplotlib==3.3.4
pip install jupyter==1.0.0
pip install numpy==1.19.5

REM notwendig für tsne
pip install scikit-learn==0.21.3
pip install sklearn==0.0
pip install ipyvolume==0.5.2

REM notwendig für Blume 
pip install seaborn==0.11.1

REM notwendig für Zeichenerkennung
pip install h5py==2.10.0

REM Libraries für die Würfelerkennung
pip install opencv-python==4.5.2.54
pip install tqdm==4.61.1

REM notwendig zum Debuggen
python -m pip install pylint

echo "Done Have a nice day and Enjoy Machine learning"
echo "If you don't have Python 3.7.x please install the right Python version first"
python -V
pause
