#include<stdio.h>
void main()
{
int a[10],b[10],c[10];
int i,m,n,j,temp;
printf("enter the limit of a:");
scanf("%d",&m);
for(i=0;i<m;i++)
{
 scanf("%d",&a[i]);
}
printf("The elements are:\n");
for(i=0;i<m;i++)
{
 printf("%d",a[i]);
}
printf("\nenter the limit of b");
scanf("%d",&n);
for(i=0;i<n;i++)
{
 scanf("%d",&b[i]);
}
printf("the array elements are:");
for(i=0;i<n;i++)
{
 printf("%d",b[i]);
}
for(i=0;i<m;i++)
{
 c[i]=a[i];
}
for(i=0;i<n;i++)
{
c[i+m]=b[i];
}
printf("\nthe element of c is");
for(i=0;i<m+n;i++)
{
 printf("%d",c[i]);
}
for(i=0;i<m+n;i++)
{
for(j=i+1;j<m+n;++j)
{
 if(c[i]>c[j])
 {
  temp=c[i];
  c[i]=c[j];
  c[j]=temp;
 }
}
}
printf("\nthe sorted array is:");
for(i=0;i<m+n;i++)
{
 printf("%d",c[i]);
}
}


