#include <QImageReader>
#include <stdio.h>

#include "colorpicker.h"

colorPicker::colorPicker(QString filename, QObject *parent)
    : QObject{parent}
{
    QImageReader reader(filename);
    this->qimage = reader.read();
}

colorPicker::~colorPicker()
{

}

int colorPicker::getMax(QVector<int> vector)
{
    int maximum = vector[0];
    int index = 0;
    for(int i = 0 ; i < 255 ; i++){
        if(vector[i] > maximum){
            maximum = vector[i];
            index = i;
        }
    }
    return index;
}

bool colorPicker::isLoaded()
{
    return !this->qimage.isNull();
}

QString colorPicker::getColor()
{
    using namespace std;
    QRgb *quadruplet;
    int width = this->qimage.width(), height = this->qimage.height();

    QVector<int> red(256), green(256), blue(256);

    for(int i = 0 ; i < height ; i++){
        quadruplet = (QRgb *)this->qimage.scanLine(i);
        for(int j = 0 ; j < width ; j++){
            red[qRed(quadruplet[j])]+=1;
            green[qGreen(quadruplet[j])]+=1;
            blue[qBlue(quadruplet[j])]+=1;
        }
    }

    int redMax = this->getMax(red), greenMax = this->getMax(green), blueMax = this->getMax(blue);

    this->dominatColor->setRgb(redMax, greenMax, blueMax);

    return this->dominatColor->name();
}

QString colorPicker::getLightColor(int factor)
{
    return this->dominatColor->lighter(factor).name();
}
