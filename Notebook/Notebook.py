import datetime;
import uuid;

class Note:
    def __init__(self, memo = '', tags = []):
        self.setMemo(memo);
        self.tags = tags;
        self.creation_date = datetime.datetime.now();
        self.id = uuid.uuid4();
    def match(self, text):
        return text in self.memo or max([text in t for t in self.tags]);
    def setMemo(self, memo = ''):
        self.memo = memo;
    def addTag(self, tag):
        self.tags.append(tag);
    def removeTag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag);
    def setTags(self, tags):
        self.tags = tags;
    def print(self):
        print('ID:      ' + str(self.id));
        print('Created: ' + self.creation_date.isoformat());
        print('Tags:    ' + ', '.join(self.tags));
        print('Memo:    ' + self.memo);


class Notebook:
    def __init__(self):
        self.notes = [];
    def new_note(self, note, tags = []):
        self.notes.append(Note(note, tags));
    def get_note(self, note_id):
        matches = [n for n in self.notes if n.id == note_id];
        if len(matches) == 0:
            return False;
        return [n for n in self.notes if n.id == note_id][0];
    def remove_note(self, note_id):
        note = self.get_note(note_id);
        if note == False:
            return False;
        self.notes.remove(note);
        return note;
    def modify_memo(self, note_id, memo):
        self.get_note(note_id).setMemo(memo);
    def modify_tags(self, note_id, tags):
        self.get_note(note_id).setTags(tags);
    def search(self, text):
        return [n for n in self.notes if n.match(text)];
