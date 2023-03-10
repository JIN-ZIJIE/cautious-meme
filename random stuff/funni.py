import tkinter as tk

root = tk.Tk()
root.title("Item Combiner")

# Create the item list
items = ["apple", "banana", "cherry"]

# Create the label that displays the current item
item_label = tk.Label(root, text="Current item: None")
item_label.pack()


def combine_items():
    global items
    if len(items) >= 2:
        new_item = items.pop() + items.pop()
        items.append(new_item)
        item_label.config(text="Current item: " + new_item)
        for item in items:
            item.pack_forget()
        for item in items:
            item.pack()
    else:
        item_label.config(text="Can't combine items")


def on_drag_start(event):
    global item_being_dragged
    item_being_dragged = event.widget


def on_drag_finish(event):
    global items, item_being_dragged
    items.remove(item_being_dragged["text"])
    item_being_dragged.pack_forget()
    item_being_dragged = None


item_being_dragged = None
for item_text in items:
    item = tk.Label(root, text=item_text, bg="white")
    item.bind("<Button-1>", on_drag_start)
    item.bind("<ButtonRelease-1>", on_drag_finish)
    item.pack()

combine_button = tk.Button(root, text="Combine", command=combine_items)
combine_button.pack()

root.mainloop()
