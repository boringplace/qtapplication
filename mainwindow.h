#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT
public:
    explicit MainWindow(QWidget *parent = 0);

signals:

public slots:
    void newFile();
    void openFile();

private:
    void createMenu();

    QAction *newAct;
    QAction *openAct;
    QMenu *fileMenu;
};

#endif // MAINWINDOW_H
