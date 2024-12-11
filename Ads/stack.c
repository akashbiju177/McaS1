#include <stdio.h>

void push();
void pop();
void peek();
int isfull();
int isempty();

int stack[100],maxsize,top=-1;
void main()
{
int choice,item;
printf("Enter the size of stack\n");
scanf("%d",&maxsize);
while(1)
{
printf("\n--- Stack Operations Menu ---\n");
printf("1. Push\n");
printf("2. Pop\n");
printf("3. Peek\n");
printf("4. Check if Full\n");
printf("5. Check if Empty\n");
printf("6. Exit\n");
printf("Enter your choice:");
scanf("%d",&choice);
switch(choice)
{
case 1: printf("Enter the element to be inserted");
        scanf("%d",&item);
        push(item);
        break;
case 2: pop();
        break;
case 3: peek();
        break;
case 4: isfull();
        break;
case 5: isempty();
        break;
case 6: printf("Exiting Program....\n");
        return;
default: printf("Invalid choice! Please try again\n");
}
}
}
int isempty()
{
if(top==-1)
{
printf("The stack is empty\n");
return 0;
}
else
{
printf("The stack is not empty\n");
return 1;
}
}
int isfull()
{
if(top==maxsize-1)
{
printf("The stack is full\n");
return 1;
}
else
{
printf("The stack is not full\n");
return 0;
}
}
void peek()
{
if(top ==-1)
{
printf("Stack is empty.No top element.\n");
}
else
{
printf("The peek of stack is %d\n",stack[top]);
}
}
void push(int data)
{
if(isfull())
{
printf("Stack Overflow! Cannot insert %d\n",data);
}
else
{
top=top+1;
stack[top]=data;
printf("The element %d is inserted\n",data);
}
}
void pop()
{
if(isempty())
{
printf("The popped element is %d\n",stack[top]);
top=top-1;
}
}
