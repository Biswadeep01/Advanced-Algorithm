#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct tree{
	int key;
	struct tree* left;
	struct tree* right;
};

struct tree* create_tree(int key){
	struct tree* temp = (struct tree*)malloc(sizeof(struct tree));
	temp->key = key;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}
void insert(struct tree* t, int key){
	if(t->key > key){
		if(t->left == NULL){
			t->left = create_tree(key);
		}else{
			insert(t->left, key);
		}
	}else{
		if(t->right == NULL){
			t->right = create_tree(key);
		}else{
			insert(t->right, key);
		}
	}
}

int height(struct tree* t){
	if(t == NULL){
		return 0;
	}else{
		int l = height(t->left);
		int r = height(t->right);
		int max = (l > r)? l : r;
		return max + 1;
	}
}

void print_tree(struct tree* t){
	if(t != NULL){
		print_tree(t->left);
		printf("%d ", t->key);
		print_tree(t->right);
	}
}

void main(){
	int val, ch;
	printf("\nEnter the root node value: ");
	scanf("%d", &val);
	struct tree* temp = create_tree(val);
	while(1){
		printf("\n1. To enter value\n2. To exit\nEnter choice: ");
		scanf("%d", &ch);
		switch(ch){
			case 1:
				printf("\nEnter the node value: ");
				scanf("%d", &val);
				insert(temp, val);
				break;
			case 2:
				printf("\n\n");
				print_tree(temp);
				exit(0);
		}
	}
}
