#include<stdio.h>
void main()
{
int a[10][10],b[10][10],c[10][10];
int i,j,k,m1,n1;
printf("Enter the no. of row of a: ");
scanf("%d",&m1);
printf("Enter the no. of columns of a: ");
scanf("%d",&n1);
printf("Enter the elements of matrix a: ");
for(i=0;i<m1;i++)
{
for(j=0;j<n1;j++)
{
scanf("%d",&a[i][j]);
}
}
printf("Enter the elements of matrix b: ");
for(i=0;i<m1;i++)
{
for(j=0;j<n1;j++)
{
scanf("%d",&b[i][j]);
}
}
for(i=0;i<m1;i++)
{
for(j=0;j<n1;j++)
{
c[i][j]=a[i][j]+b[i][j];
}
}
printf("addition of matrix  is: ");
for(i=0;i<m1;i++)
{
for(j=0;j<n1;j++)
{
printf("%d ",c[i][j]);
}
}
for(i=0;i<m1;i++)
{
for(j=0;j<n1;j++)
{
c[i][j]=a[i][j]-b[i][j];
}
}
printf("\nsubtraction matrix is: ");
for(i=0;i<m1;i++)
{
for(j=0;j<n1;j++)
{
printf("%d ",c[i][j]);
}
}
for(i = 0; i < m1; i++) 
{
for(j = 0; j < n1; j++) 
{
c[i][j] = 0;
for(k = 0; k < n1; k++)
{
c[i][j] += a[i][k] * b[k][j];
}
}
}
printf("\nmultiplication matrix c is: ");
for(i=0;i<m1;i++)
{
for(j=0;j<n1;j++)
{
printf("%d ",c[i][j]);
}
}
}

