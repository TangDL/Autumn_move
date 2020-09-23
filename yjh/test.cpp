#include "bits/stdc++.h"

using namespace std;

void st(vector<char>& array, int start, int last){
    int i = start;
    int j = last;
    int temp = array[i];
    if (i < j){
        while (i < j){
            while (i < j &&  array[j]>=temp )
                j--;
            if (i < j){
                array[i] = array[j];
                i++;
            }
            while (i < j && temp > array[i])
                i++;
            if (i < j){
                array[j] = array[i];
                j--;
            }
        }
        array[i] = temp;
        st(array, start, i - 1);
        st(array, i + 1, last);
    }
}
int denoise_histeq(const unsigned char *srcImage, unsigned char *dstImage, int width, int height){ 
    vector<vector<char>> src(height,vector<char>(width)); 
    vector<vector<char>> dst(height,vector<char>(width));
    for(int i=0;i<height;i++){
        for(int j=0;j<width;j++){
            src[i][j]= srcImage[i*width+j];
            dst[i][j]= srcImage[i*width+j];
        }
    }
    int k_size = 7;
    vector<int> kernel(k_size*k_size);
    for(int i=3;i<height-3;i++){
        for(int j=3;j<width-3;j++){
            vector<char> tmp;
            for(int k=-3;k<=3;k++){
                for(int m=-3;m<=3;m++){
                tmp.push_back(src[i+k][j+m]);   // 获取以（i,j）为中心的像素矩阵，储存为向量方便排序tmp
                }
            }
            st(tmp,0, tmp.size()-1);            // 对tmp进行排序，取中间值为（i, j）新得像素值
            dst[i][j]=tmp[k_size*k_size/2];
        }
    }
    vector<int> gray(256);
    vector<double> gray_p(256);
    vector<double> gray_d(256);
    vector<int> gray_e(256);
    for(int i=0;i<height;i++){
        for(int j=0;j<width;j++){
            int value = dst[i][j];
            gray[value]++;  // 统计各灰度像素的个数
        }
    }
    for(int i=0;i<256;i++){
        gray_p[i] = ((double)gray[i]/(width*height));   // 计算各灰度级的概率
    }
    gray_d[0]=gray_p[0];
    for(int i=1;i<256;i++){
        gray_d[i] = gray_d[i-1]+gray_p[i];             // 计算各灰度级概率的累加值，最后一个灰度级的累计值为1
    }
    for(int i=1;i<256;i++){
        gray_e[i]=char(255*gray_d[i]+0.5);      // 根据映射关系求取像素值
    }
    for(int i=0;i<height;i++){
        for(int j=0;j<width;j++){
            dst[i][j] = gray_e[dst[i][j]];
            dstImage[i*width+j] = dst[i][j];
        }
    }
    return 0;
}
