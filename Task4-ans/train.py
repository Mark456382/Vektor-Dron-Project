from network import gen_model, x_test, y_test, x_train, y_train

# Обучение и сохранение модели

model = gen_model()
model.fit(x_train,
          y_train,
          batch_size=64,
          epochs=10,
          validation_data=(x_test, y_test))
model.save(str(input('Куда сохранть обученную модель? => '))+'model.h5')
