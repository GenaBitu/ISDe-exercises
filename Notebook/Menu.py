from Notebook import Note, Notebook;
import uuid;

class Menu:
    def __init__(self):
        self.notebook = Notebook();
        self.notebook.new_note('Example note', ['Example tag 1', 'Example tag 2']);
    def run(self):
        self.showMenu();
        self.waitForInput();
    def showMenu(self):
        print();
        print('Notebook Menu');
        print('-------------');
        print('Choose action:');
        print('1 - Show all notes');
        print('2 - Search notes');
        print('3 - Add a note');
        print('4 - Modify a note');
        print('5 - Quit');
    def waitForInput(self):
        option = input('Action: ');
        if option == '1':
            self.showNotes();
        elif option == '2':
            self.searchNote();
        elif option == '3':
            self.addNote();
        elif option == '4':
            self.modifyNote();
        elif option != '5':
            print('Please choose a valid action.');
            self.waitForInput();
    def printNotes(self, notes):
        first = True;
        for note in notes:
            if not first:
                print();
            first = False;
            note.print();
    def showNotes(self):
        print();
        print('All notes');
        print('---------');
        if len(self.notebook.notes) == 0:
            print('There are no notes.');
        else:
            self.printNotes(self.notebook.notes);
        self.run();
    def searchNote(self):
        print();
        print('Search for a note');
        print('-----------------');
        text = input('Search for: ');
        result = self.notebook.search(text);
        if len(result) == 0:
            print("No notes found.");
        else:
            print();
            print('Results');
            print('-------');
            self.printNotes(self.notebook.search(text));
        self.run();
    def addNote(self):
        print();
        print('Add a note');
        print('----------');
        memo = input('Enter a note: ');
        self.saveNoteDialog(Note(memo));
    def saveNoteDialog(self, note):
        print();
        print('Save note?');
        print('----------');
        self.printNotes([note]);
        print();
        print('Choose action:');
        print('1 - Save');
        print('2 - Edit');
        print('3 - Add a tag');
        print('4 - Remove a tag');
        self.waitForNoteSaveInput(note);
    def waitForNoteSaveInput(self, note):
        action = input('Action: ');
        if action == '1':
            self.notebook.notes.append(note);
            print('Note saved.');
            self.run();
        elif action == '2':
            self.editNote(note);
        elif action == '3':
            self.addNoteTag(note);
        elif action == '4':
            self.removeNoteTag(note);
        else:
            print('Please choose a valid action.');
            self.waitForNoteSaveInput(note);
    def editNote(self, note):
        print();
        print('Edit a note');
        print('-----------');
        text = input('New note: ');
        note.setMemo(text);
        self.saveNoteDialog(note);
    def addNoteTag(self, note):
        print();
        print('Add note tag');
        print('------------');
        tag = input('Tag: ');
        note.addTag(tag);
        self.saveNoteDialog(note);
    def removeNoteTag(self, note):
        print();
        print('Remove note tag');
        print('---------------');
        tag = input('Tag: ');
        note.removeTag(tag);
        self.saveNoteDialog(note);
    def modifyNote(self):
        print();
        print('Modify a note');
        print('-------------');
        self.waitForNoteModifyInput();
    def waitForNoteModifyInput(self):
        note_id = input('Note id: ');
        note = self.notebook.remove_note(uuid.UUID(note_id));
        if note == False:
            print('Note not found.');
            self.waitForNoteModifyInput();
        else:
            self.saveNoteDialog(note);

