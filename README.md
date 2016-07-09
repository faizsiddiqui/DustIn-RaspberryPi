1. Create samples
```cmd
perl ML/tools/createsamples.pl positives.txt negatives.txt samples 1500 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 50 -h 70"
```
2. Create .vec files from samples
```cmd
python ML/tools/mergevec.py -v samples/ -o samples.vec
```
3. Train
```cmd
opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 5 -w 50 -h 70 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024
```
