#include <stdio.h>
struct Student {
char name[50];
int id;
int age;
};
int main()
{
struct Student student = {"Steeve",135,21};
printf("Student Details:\n");
printf("Name:%s\n",student.name);
printf("ID:%d\n",student.id);
printf("Age:%d\n",student.age);
return 0;
}

