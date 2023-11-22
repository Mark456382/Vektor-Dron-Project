from task4 import gen_model, x_test, y_test, x_train, y_train

# Обучение модели и сохранение модели

model = gen_model()
model.fit(x_train,
        y_train,
        batch_size=128,
        epochs=10,
        verbose=1,
        validation_data=(x_test, y_test))
model.save(str(input('Куда сохранть обученную модель? => '))+'model.h5')
