class SingletonPattern {

    private static instance: SingletonPattern;

    public static getInstance = () => {
        if (!SingletonPattern.instance) {
            SingletonPattern.instance = new SingletonPattern();
        }

        return SingletonPattern.instance;
    }
}

const main = () => {
    const singletonObjOne = SingletonPattern.getInstance();
    const singletonObjTwo = SingletonPattern.getInstance();

    if (singletonObjOne === singletonObjTwo) {
        console.log("valid");
    }
}

main();