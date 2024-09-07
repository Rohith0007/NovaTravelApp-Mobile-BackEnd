# NovaTravelApp

## Backend

    python manage.py migrate    

    python manage.py runserver



## FrontEnd
info 💡 To enable automatic CocoaPods installation when building for iOS you can create react-native.config.js with automaticPodsInstallation field. 
For more details, see https://github.com/react-native-community/cli/blob/main/docs/projects.md#projectiosautomaticpodsinstallation
            
✔ Initializing Git repository

  
  Run instructions for Android:
    • Have an Android emulator running (quickest way to get started), or a device connected.
    • cd "/Users/rohithgupthakona/NOVA-Versions/NovaTravelApp/view" && npx react-native run-android
  
  Run instructions for iOS:
    • cd "/Users/rohithgupthakona/NOVA-Versions/NovaTravelApp/view/ios"
    
    • Install Cocoapods
      • bundle install # you need to run this only once in your project.
      • bundle exec pod install
      • cd ..
    
    • npx react-native run-ios
    - or -
    • Open view/ios/view.xcodeproj in Xcode or run "xed -b ios"
    • Hit the Run button
    
  Run instructions for macOS:
    • See https://aka.ms/ReactNativeGuideMacOS for the latest up-to-date instructions.


    emulator -avd Pixel_3a_API_34_extension_level_7_arm64-v8a
    
    npx react-native run-android  # For Android
    npx react-native run-ios  # For iOS