#ifndef COLORPICKER_H
#define COLORPICKER_H

#include <QObject>
#include <QImage>
#include <QVector>

class colorPicker : public QObject
{
    Q_OBJECT
public:
    explicit colorPicker(QString filename, QObject *parent = nullptr);
    ~colorPicker();
    int getMax(QVector<int> vector);
    bool isLoaded();
    QString getColor();
    QString getLightColor(int factor = 150);

signals:

private:
    QImage qimage;
    QColor *dominatColor;

};

#endif // COLORPICKER_H
