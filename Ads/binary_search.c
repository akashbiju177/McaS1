#include<stdio.h>
void main()
{
int arr[10],i,left=0,right,size,search,middle;
printf("enter the limit\n");
scanf("%d",&size);
right=size-1;
printf("enter the numbers\n");
for(i=0;i<size;i++)
{
scanf("%d",&arr[i]);
}
printf("entered array = ");
for(i=0;i<size;i++)
{
printf("%d \n",arr[i]);
}
printf("enter the element to be found");
scanf("%d",&search);

while(left<=right)
{
middle=(left+right)/2;
if(arr[middle]==search)
{
printf("the element is found at location %d",middle);
break;
}
else if(arr[middle]>search)
{
right=middle-1;
}
else
{
left=middle+1;
}
}
if(left>right)
{
printf("element not found in the list");
}
}
