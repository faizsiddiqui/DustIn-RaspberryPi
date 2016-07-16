Machine learning Steps
----------------------

1. **List positive and negative image in text file**
	-	**Linux**
	```cmd
	find ./positive_images -iname "*.jpg" > positives.txt
	find ./negative_images -iname "*.jpg" > negatives.txt
	```
	-	**Windows**
	```cmd
	forfiles /s /m *.jpg /c "cmd /c echo @relpath" > positives.txt
	forfiles /s /m *.jpg /c "cmd /c echo @relpath" > negatives.txt
	```
	** Remove quotes in the files.**

        ** Replace .\ -> ./positive_images/ **  

2. **Create samples**
```cmd
perl ML/tools/createsamples.pl positives.txt negatives.txt samples 1500 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 50 -h 70"
```

3. **Create .vec files from samples**
```cmd
python ML/tools/mergevec.py -v samples/ -o samples.vec
```

4. **Train**
```cmd
opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 5 -w 50 -h 70 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024
```

More information here :
- [opencv-haar-classifier-training](https://github.com/mrnugget/opencv-haar-classifier-training)
- [Train your own OpenCV Haar Classifier](http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html)