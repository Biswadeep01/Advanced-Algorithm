#include<stdio.h>
#include<stdlib.h>
#define GSIZE 20
#define WHITE 0
#define GRAY 1
#define BLACK 2

struct queue{
	int front;
	int rear;
	int arr[50];
};

void create_queue(struct queue* q){
	q->front = 0;
	q->rear = -1;
}
void insert_queue(struct queue* q, int key){
	q->rear=q->rear+1;
	q->arr[q->rear] = key;
}
int delete_queue(struct queue* q){
	int val = q->arr[q->front];
	q->front = q->front + 1;
	return val;
}
bool empty_queue(struct queue* q){
	if(q->rear < q->front){
		return true;
	}
	return false;
}

struct graph{
	int adj[GSIZE][GSIZE];
	int ver;
	int bfsdist[GSIZE];
	int bfspred[GSIZE];
	int bfscol[GSIZE];
};

