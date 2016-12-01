function err(errString) {
        alert(errString);
}

var myFolder = Folder("/Users/bdds/Projects/ReverieHologram/output/");

var myProject = app.newProject();
var myImportOptions = new ImportOptions();
myImportOptions.sequence = true
myImportOptions.forceAlphabetical = true;

var myFiles = myFolder.getFiles();

for(var i=0; i<myFiles.length; i++) {
        //console.log("yo");
        myImportOptions.file = myFiles[i];
        app.project.importFile(myImportOptions);
}

// myImportOptions.canImportAs(ImportAsType.FOOTAGE);

// myImportOptions().file = File("/c/Users/bdds/Projects/ReverieHologram/Template Comp.mov");

//var myFootage = app.project.importFile(myImportOptions);

// opens app main window and brings it to the front of the desktop
app.activate();
