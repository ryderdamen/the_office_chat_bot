<?php
/* 	Name: processor.php
	Author: Ryder Damen | ryderdamen.com
	Description: This processes the raw text transcript files into JSON and parsed text. It removes white space, names, etc.
*/

$files = array_diff(scandir('raw/'), array('.', '..'));
foreach($files as $file) {
    processFile($file);
}
echo "Files have been processed and saved!" . PHP_EOL;
die;

function processFile($fileName) {
    // Get the contents, and clean the data
    $contents = file_get_contents('raw/' . $fileName);
    $contents = preg_replace('/\[.*\]/', '', $contents); // Remove everything in square brackets
    $contents = removeNames($contents); // Remove names
    $contents = str_ireplace('\n\n\n\n', '\n\n', $contents); // Remove extra whitespace
    $contents = str_ireplace('\n\n\n', '\n\n', $contents); // Remove extra whitespace
    $contents = str_ireplace('\s\s', '\s', $contents); // Replace extra spaces
    $contents = str_ireplace('---', '...', $contents); // replace --- with elips
    $contents = removeExtraLinesAndSpaces($contents);
    $contents = ltrim($contents);
    writeTxtFile($contents, $fileName);
    writeJsonFile($contents, $fileName);
}

function removeNames($contents) {
    return preg_replace('/(?<=\n)(.*?)[?=\:]\s/', '', $contents); // Remove everything in square brackets
}

function removeExtraLinesAndSpaces($contents) {
    return preg_replace('/[ \t]+/', ' ', preg_replace('/\s*$^\s*/m', "\n", $contents));
}

function writeTxtFile($contents, $fileName) {
    $myfile = fopen("processed/txt/" . $fileName, "w") or die("Unable to open file!");
    fwrite($myfile, $contents);
    fclose($myfile);
}

function writeJsonFile($contents, $fileName) {
    $json = json_encode( explode(PHP_EOL, $contents), JSON_PRETTY_PRINT);
    $myfile = fopen("processed/json/" . str_ireplace('.txt', '.json', $fileName), "w") or die("Unable to open file!");
    fwrite($myfile, $json);
    fclose($myfile);
}