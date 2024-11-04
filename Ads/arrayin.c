#include<stdio.h>
void main()
{
 int a[10],i,n,pos,in;
 printf("enter the limit");
 scanf("%d",&n);
 printf("enter the numbers");
 for(i=0;i<n;i++)
 {
  scanf("%d",&a[i]);
 }
 printf("enter the element to be inserted");
 scanf("%d",&in);
 printf("enter the position to be inserted");
 scanf("%d",&pos);
 for(i=n;i>=pos;i--)
 {
  a[i]=a[i-1];
 }
 a[pos-1]=in;
 printf("Array after deletion:");
 for(i=0;i<n+1;i++)
 {
 printf("%d",a[i]);
}
}
