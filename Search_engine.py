'''
Author:Akhilesh Dhama
Date:16-Sept-2021
Purpose:Practice 7
'''

#to compile list of items in which search item is present in relevence manner
def compiled_result(search_item,list):
    rough_list=searched_item_in_list(search_item,list)
    search_item=search_item.split()
    
    final_list=[]
# descended order final list
    for item in search_item:
        relevance=0

        for word in rough_list:
            items_in_str=word.split()
            itr_relevance=items_in_str.count(item)
            if itr_relevance>=relevance:
                relevance=itr_relevance
        for i in range(len(rough_list)):
            for word in rough_list:
                items_in_str=word.split()
                if relevance==items_in_str.count(item) and word not in final_list:
                    final_list.append(word)
            relevance-=1
    return final_list

# for list of items in list in which items are present in rough manner
def searched_item_in_list(search_item,list):
    searched_item_in_list_list=[]
    search_item=search_item.split()

    for item in search_item:

        for word in list:
            if item in word and word not in searched_item_in_list_list:
                searched_item_in_list_list.append(word)
    return searched_item_in_list_list

# what you want to with the above functions     
if __name__=="__main__":
    import time
    mylist=["this is good","python is good","python is not a python snake"]
    searched=input("Enter the word to search:\n").lower()
    final_result=compiled_result(searched,mylist)
    if len(final_result)==0:
        print(f"No keyword found ({time.process_time()}s)")
    else:
        print(f"{len(final_result)} results found ({time.process_time()}s)")
        for i in final_result:
            print(i)

