# load db.reset.json
with open('db.reset.json', 'r') as file:
    reset_task = json.load(file)
    reset_task.sort(key=lambda x: x['finalized'], reverse=False)

    # save the db.reset in db to reset it
    with open('db.json', 'w') as file:
        json.dump(reset_task, file, indent=4)