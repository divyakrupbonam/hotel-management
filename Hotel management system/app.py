from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

# Room data (room number, guest name, check-in status, and price)
rooms = {
    101: {
        "price": 120,
        "status": "Available",
        "guest_name": "",
        "image": "https://i.pinimg.com/736x/a7/92/28/a792280c9521b9f53d904eb173dc6993.jpg"
    },
    102: {
        "price": 150,
        "status": "Occupied",
        "guest_name": "John Doe",
        "image": "https://i.pinimg.com/474x/98/e2/02/98e202e8c27f0283950d3191c92d4fe1.jpg"
    },
    103: {
        "price": 180,
        "status": "Available",
        "guest_name": "",
        "image": "https://i.pinimg.com/474x/5b/50/16/5b50165748510841b16fd6ac6eda378b.jpg"
    },
    104: {
        "price": 130,
        "status": "Available",
        "guest_name": "",
        "image": "https://i.pinimg.com/474x/0c/63/9f/0c639f6d8615f410e0d118b93575a727.jpg"
    },
    105: {
        "price": 200,
        "status": "Occupied",
        "guest_name": "Alice Smith",
        "image": "https://i.pinimg.com/474x/2a/4c/54/2a4c54792538ccd8452404422db2f648.jpg"
    },
    106: {
        "price": 160,
        "status": "Available",
        "guest_name": "",
        "image": "https://i.pinimg.com/474x/0b/5c/1a/0b5c1aa9370b77858ff2420e9bc1449f.jpg"
    }
}


@app.route('/')
def index():
    return render_template('index.html', rooms=rooms)

@app.route('/checkin', methods=['POST'])
def check_in():
    room_num = int(request.form['room_num'])
    guest_name = request.form['guest_name']
    
    # Check if the room exists
    if room_num not in rooms:
        flash("Room does not exist!")
        return redirect(url_for('index'))

    if rooms[room_num]["status"] == "Occupied":
        flash("Room is already occupied!")
        return redirect(url_for('index'))
    
    rooms[room_num]["guest_name"] = guest_name
    rooms[room_num]["status"] = "Occupied"
    flash(f"Checked in guest {guest_name} to Room {room_num}")
    return redirect(url_for('index'))

@app.route('/checkout', methods=['POST'])
def check_out():
    room_num = int(request.form['room_num'])
    
    # Check if the room exists
    if room_num not in rooms:
        flash("Room does not exist!")
        return redirect(url_for('index'))

    if rooms[room_num]["status"] == "Available":
        flash("Room is already vacant!")
        return redirect(url_for('index'))
    
    guest_name = rooms[room_num]["guest_name"]
    rooms[room_num]["guest_name"] = ""
    rooms[room_num]["status"] = "Available"
    flash(f"Checked out guest {guest_name} from Room {room_num}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



