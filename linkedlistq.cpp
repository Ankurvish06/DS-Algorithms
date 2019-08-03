#https://practice.geeksforgeeks.org/problems/union-of-two-linked-list/1

struct node* makeUnion(struct node* head1, struct node* head2)
{
    set<int,greater<int>> v,v1;
    int i,j,k;
    while(head1!=NULL){
        v.insert(head1->data);
        head1 = head1->next;
    }
    while(head2!=NULL){
        v1.insert(head2->data);
        head2 = head2->next;
    }
    v1.insert(v.begin(),v.end());
    node* head = NULL;
    set<int,greater<int>>::iterator it;
    for(it=v1.begin();it!=v1.end();it++){
        push(&head,*it);
    }
    return head;
}
