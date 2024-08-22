import mido


def list_notes_from_midi(file_path):
    midi = mido.MidiFile(file_path)
    current_instruments = {}
    all_notes = []


    for track in midi.tracks:
        absolute_time = 0
        for msg in track:
            absolute_time += mido.tick2second(msg.time, midi.ticks_per_beat, mido.bpm2tempo(100))  # 187
            # absolute_time += dt
            if msg.type == 'program_change':
                current_instruments[msg.channel] = msg.program
            if msg.type == 'note_on' and msg.velocity > 0:
                note_name = msg.note
                instrument = current_instruments.get(msg.channel, 0)  # Default to instrument 0 if not set
                all_notes.append({
                    'name': note_name,
                    'start_time': absolute_time,
                    'instrument': instrument,
                    'velocity' : msg.velocity,
                    'play' : False
                })
            if msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                note_name = msg.note
                instrument = current_instruments.get(msg.channel, 0)  # Default to instrument 0 if not set
                all_notes.append({
                    'name': note_name,
                    'start_time': absolute_time,
                    'instrument': instrument,
                    'velocity': 0,
                    'play': False
                })

    return all_notes
