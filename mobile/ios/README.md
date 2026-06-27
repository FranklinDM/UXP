# Dactyloidae iOS

This code only works with Xcode 9.2 and supports iOS 10 and above.

This code is written in Swift 3.2.

## Building the code

1. Install the latest [Xcode developer tools](https://developer.apple.com/xcode/downloads/) from Apple.
2. Install Carthage
    ```shell
    brew update
    brew install carthage
    ```
3. Clone the repository:
    ```shell
    git clone https://repo.dactyloidae.xyz/dactyloidae/dactyloidae
    ```
4. Pull in the project dependencies:
    ```shell
    cd dactyloidae/mobile/ios
    sh ./bootstrap.sh
    ```
5. Open `Client.xcodeproj` in Xcode.
6. Build the `Fennec` scheme in Xcode.
