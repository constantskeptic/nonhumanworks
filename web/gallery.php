<?php
error_reporting(E_ALL);
echo '<link rel="stylesheet" href="styles.css">';
echo '<meta name="viewport" content="width=device-width, initial-scale=1">';
ini_set("display_errors", 1);
        $dirname = "static/";
        $images = scandir($dirname);
        // shuffle($images);
    $ignored = array('.', '..', '.svn', '.htaccess');


function scan_dir($dir) {
    $ignored = array('.', '..', '.svn', '.htaccess');

    $files = array();    
    foreach (scandir($dir) as $file) {
        if (in_array($file, $ignored)) continue;
        $files[$file] = filemtime($dir . '/' . $file);
    }

    arsort($files);
    $files = array_keys($files);

    return ($files) ? $files : false;
}

$filer = scan_dir($dirname);
        $ignore = Array(".", "..");
        foreach($filer as $curimg){
            if(!in_array($curimg, $ignore)) {
                echo "<li><a title='".$curimg."' href='".$dirname.$curimg."'><img width='256' src='".$dirname.$curimg."' alt='' /></a></li>\n";
            }
        }                 
?>

