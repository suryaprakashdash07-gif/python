#include <stdio.h>
#include <string.h>

#define MAX_DATA_SIZE 1024
#define FLAG 0x7E
#define ESC 0x7D

// Function for Character Framing
void characterFraming(char data[], int length)
{
    printf("Character Framing:\n");
    printf("Frame: %c", FLAG);

    for (int i = 0; i < length; i++)
    {
        printf("%c", data[i]);
    }

    printf("%c\n", FLAG);
}

// Function for Character Stuffing
void characterStuffing(char data[], int length)
{
    printf("Character Stuffing:\n");
    printf("Frame: %c", FLAG);

    for (int i = 0; i < length; i++)
    {
        if (data[i] == FLAG)
        {
            printf("%c%c", ESC, FLAG);
        }
        else
        {
            printf("%c", data[i]);
        }
    }

    printf("%c\n", FLAG);
}

// Function for Bit Stuffing
void bitStuffing(char data[], int length)
{
    printf("Bit Stuffing:\n");

    int consecutiveOnes = 0;

    for (int i = 0; i < length; i++)
    {
        printf("%c", data[i]);

        if (data[i] == '1')
        {
            consecutiveOnes++;
        }
        else
        {
            consecutiveOnes = 0;
        }

        if (consecutiveOnes == 5)
        {
            printf("0");
            consecutiveOnes = 0;
        }
    }

    printf("\n");
}

int main()
{
    char data[MAX_DATA_SIZE];
    int length;

    printf("Enter the data: ");
    fgets(data, MAX_DATA_SIZE, stdin);

    length = strlen(data) - 1;

    printf("\nOriginal Data: ");
    for (int i = 0; i < length; i++)
    {
        printf("%c", data[i]);
    }
    printf("\n");

    characterFraming(data, length);
    characterStuffing(data, length);
    bitStuffing(data, length);

    return 0;
}