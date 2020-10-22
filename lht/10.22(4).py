#include <ctype.h>
#include <stdio.h>
void itoa (int n,char s[]);
//atoi 函数：将ｓ转换为整形数
int main(void)
{
    int n;
    char s[100];
    printf("Input n:\n");
    scanf("%d",&n);
    printf("the string : \n");
    itoa (n,s);
    return 0;
}
void itoa (int n,char s[])
{
    int i,j,sign;
    if((sign=n)<0)//记录符号
    n=-n;//使n成为正数
    i=0;
    do{
           s[i++]=n%10+'0';//取下一个数字
    }
    while ((n/=10)>0);//删除该数字
    if(sign<0)
    s[i++]='-';
    s[i]='\0';
    for(j=i;j>=0;j--)//生成的数字是逆序的，所以要逆序输出
           printf("%c",s[j]);
}
